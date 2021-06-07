from cbuild.util import make

def do_configure(self):
    self.do(
        self.chroot_build_wrksrc / self.configure_script,
        self.configure_args, build = True
    )

def do_build(self):
    self.make = make.Make(self)
    self.make.build()

def do_check(self):
    pass

def do_install(self):
    self.make.install()

def use(tmpl):
    tmpl.build_style = "configure"
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install
