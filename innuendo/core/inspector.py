import inspect, cProfile, pstats, StringIO
import yaml
import time

exclusions = ('__builtins__', '__doc__', '__file__')
meta = {'__name__': None , '__package__': None}

entities_visited = set() 

def execution_time():
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))


def wrapper(parent, name, func):
    def func_wrapper(*args, **kwargs):
        
        try:
            s = StringIO.StringIO()
            sortby = 'cumulative'
        except Exception as e:
            print e

        try:

            start_time = time.time()
            # Start profiling
            try:
                pr = cProfile.Profile()
                pr.enable()
            except Exception as e:
                print 'exc the profiler'

            ret = func(*args, **kwargs)

            # Stop profiling
            try:
                pr.disable()

                

                ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
                ps.print_stats()
                print s.getvalue()

                print '--- func: %s.%s spent %s seconds ---' % (parent.__name__, name,time.time() - start_time)
            except Exception as e:
                print '--- func: %s.%s spent %s seconds ---' % (parent.__name__, name,time.time() - start_time)
                print 'exc the profiler en disable'

            return ret
        except Exception as e:
            print '----- Unhandled exception: %s -----' % (e)

            # Stop profiling
            try:
                pr.disable()

                ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
                ps.print_stats()
                print s.getvalue()
                print '--- func: %s.%s spent %s seconds ---' % (parent.__name__, name,time.time() - start_time)
            except Exception as e:
                print 'exc the profiler en disable'

            raise e

    return func_wrapper

def get_members(parent):
    members = inspect.getmembers(parent)

    for m in members:
        if isinstance(m, tuple) and m[0] not in exclusions:
            if m[0] in meta:
                meta[0] = m[1]
            else:
                decorate(parent, m)

def decorate(parent, element):
    name = element[0]
    value = element[1]

    if inspect.ismodule(value):
        print 'module %s' % (name)
        if name not in entities_visited:
            entities_visited.add(name)
            get_members(value)
    elif inspect.isclass(value):
        print 'class %s' % (name)
        if name not in entities_visited:
            entities_visited.add(name)
            get_members(value)
    elif inspect.ismethod(value):
        setattr(parent, name, wrapper(parent, name, value))
    elif inspect.isfunction(value):
        setattr(parent, name, wrapper(parent, name, value))


def load_config(file_path):
    stream = file(file_path, 'r')    # 'document.yaml' contains a single YAML document.
    conf = yaml.load(stream)

    return conf

def main():
    import sys, imp, os

    conf = load_config('exclusions.yaml')

    print conf

    entities_visited.update(conf.get('base', []))

    print entities_visited

    module_name = sys.argv[1]
    path = os.path.dirname(os.path.abspath(__file__))

    #from django.core.management.commands import runserver as module

    module = imp.load_source(module_name.split('.py')[0], '{}/{}'.format(path, module_name))
    
    get_members(module)

    #module.__name__ = '__main__'

    module.main()
    
    #module.BaseRunserverCommand.run()

    #os.system('python manage.py runserver')

if __name__ == '__main__':
    main()
    
    
            
