from cbuild.util import linux


def configure(self):
    linux.configure(self, self.configure_args, env=self.configure_env)


def build(self):
    renv = dict(self.make_env)
    renv.update(self.make_build_env)
    linux.build(self, renv)


def install(self):
    renv = dict(self.make_env)
    renv.update(self.make_install_env)
    linux.install(self, renv)


def use(tmpl):
    tmpl.configure = configure
    tmpl.build = build
    tmpl.install = install
