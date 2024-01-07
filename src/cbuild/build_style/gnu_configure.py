from cbuild.util import gnu_configure, make


def do_configure(self):
    gnu_configure.replace_guess(self)
    gnu_configure.configure(self)


def do_build(self):
    self.make.build()


def do_check(self):
    self.make.check()


def do_install(self):
    self.make.install()


def use(tmpl):
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.make = make.Make(tmpl, env=gnu_configure.get_make_env())
    tmpl.build_style_defaults = [
        ("make_dir", "build"),
        ("configure_gen", ["autoreconf", "-if"]),
    ]
