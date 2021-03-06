class Parser:
    def __init__(self, irc, handler, path):
        self.irc = irc
        self.path = path
        self.handler = handler

    def do_imports(self):
        if len(self.handler.delayed_imports) > 0:
            for imp in self.handler.delayed_imports:
                self.handler.load_module(imp, delay=False)
                self.handler.delayed_imports.remove(imp)

    def do_unloads(self):
        du_len = len(self.handler.delayed_unloads)
        if du_len > 0:
            for x in range(len(self.handler.delayed_unloads)):
                um_len = len(self.handler.delayed_unloads)
                self.handler.unload_module(self.handler.delayed_unloads.pop(), delay=False)
                if len(self.handler.delayed_unloads) != um_len:
                    self.irc.message("Unloaded module")
                else:
                    self.irc.message("rarely seen error message, might be about unloading")

    def run(self, line):
        if isinstance(line[1], list):
            line[1][-1] = line[1][-1].replace("\r\n", "")
            #line[1][0] = line[1][0].lstrip(':')
            line[1][0] = line[1][0][1:]
        for key, module in self.handler.importlist.iteritems():
            if line[1] != None:
                data = [word.lstrip() for word in line[1]]
                try:
                    module.main(self.irc, line[0], data, self.handler)
                except SyntaxError:
                    pass
        self.do_imports()
        self.do_unloads()
