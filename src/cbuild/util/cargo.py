import re

def clear_vendor_checksums(pkg, crate, vendor_dir = "vendor"):
    p = (self.cwd / vendor_dir / crate / ".cargo-checksum.json")
    p.write_text(re.sub(r"""("files":{)[^}]*""", r"\1", p.read_text()))
