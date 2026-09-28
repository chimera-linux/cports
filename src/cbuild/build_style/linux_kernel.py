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


def _update_configs(self):
    linux.update_configs(self, self.archs, self.configure_args)


def use(tmpl):
    tmpl.configure = configure
    tmpl.build = build
    tmpl.install = install
    tmpl._custom_targets["generate-configs"] = (_update_configs, "patch")
