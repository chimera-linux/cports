url = "https://git.savannah.gnu.org/cgit/readline.git/log"
pattern = r">Readline-([\d\.]+\spatch\s\d+)"


def fetch_versions(self, src):
    def remapmesenpai(v):
        # truncate garbage
        ver = v.replace(" patch ", ".")
        # pad .7 -> .007
        bigver, patch = ver.rsplit(".", 1)
        zeropatch = patch.zfill(3)
        return f"{bigver}.{zeropatch}"

    return map(remapmesenpai, self.fetch_versions(src))
