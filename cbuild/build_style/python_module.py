def do_build(self):
    self.do("python", ["setup.py", "build"] + self.make_build_args)

def do_check(self):
    pass

def do_install(self):
    self.do(
        "python", [
            "setup.py", "install", "--prefix=/usr",
            "--root=" + str(self.chroot_destdir)
        ] + self.make_install_args
    )

def use(tmpl):
    tmpl.build_style = "python_module"
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install
