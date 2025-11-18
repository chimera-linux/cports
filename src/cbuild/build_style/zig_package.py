from cbuild.util import zig_package


def use(tmpl):
    tmpl.do_install = zig_package.install
