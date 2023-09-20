from cbuild.util import make, meson


def do_configure(self):
    meson.configure(self, self.meson_dir)


def do_build(self):
    self.make.build()


def do_check(self):
    meson.check(self)


def do_install(self):
    meson.install(self)


def use(tmpl):
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.make = make.Make(tmpl)

    tmpl.build_style_defaults = [
        ("make_cmd", "ninja"),
        ("make_build_target", "all"),
        ("make_check_target", "test"),
        ("make_dir", "build"),
    ]
