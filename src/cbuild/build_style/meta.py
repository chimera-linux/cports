def fetch(self):
    if len(self.source) > 0:
        self.error("meta build style cannot define sources")


def install(self):
    pass


def use(tmpl):
    tmpl.fetch = fetch
    tmpl.install = install
