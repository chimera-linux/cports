def do_fetch(self):
    pass


def do_install(self):
    pass


def use(tmpl):
    tmpl.do_fetch = do_fetch
    tmpl.do_install = do_install
