# -*- coding: utf-8 -*-
"""
Entry Point for the agent app
"""

from innuendo.core.interface import TerminalInterface

def main():
    """
    Main function that creates a Terminal Object and run it
    """

    app = TerminalInterface()
    app.run()

if __name__ == '__main__':
    main()
