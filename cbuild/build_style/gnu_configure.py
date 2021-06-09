from cbuild.util import make

benv = {
    "lt_cv_sys_lib_dlsearch_path_spec": \
        "/usr/lib64 /usr/lib32 /usr/lib /lib /usr/local/lib"
}

def init_configure(self):
    self.make = make.Make(self, env = benv)

def do_configure(self):
    self.do(
        self.chroot_build_wrksrc / self.configure_script,
        self.configure_args, build = True, env = benv
    )

def do_build(self):
    self.make.build()

def do_check(self):
    pass

def do_install(self):
    self.make.install()

def use(tmpl):
    tmpl.build_style = "gnu_configure"
    tmpl.init_configure = init_configure
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install
