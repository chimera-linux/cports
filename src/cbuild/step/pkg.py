from cbuild.core import template


def invoke(pkg):
    template.call_pkg_hooks(pkg, "do_pkg")
    template.call_pkg_hooks(pkg, "post_pkg")
