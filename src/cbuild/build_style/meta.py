def do_fetch(self):
    if len(self.source) > 0:
        self.error("meta build style cannot define sources")


def do_install(self):
    pass


def use(tmpl):
    tmpl.do_fetch = do_fetch
    tmpl.do_install = do_install
