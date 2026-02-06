from cbuild.util import zig_build


def do_build(self):
    zig_build.build(self, self.zig_build_args)


def do_install(self):
    zig_build.install(self)


def use(tmpl):
    tmpl.do_build = do_build
    tmpl.do_install = do_install
