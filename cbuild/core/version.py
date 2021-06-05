# implements the same version comparison algorithm as xbps

mods = {
    "alpha": -3,
    "beta": -2,
    "pre": -1,
    "rc": -1,
    "pl": 0,
    ".": 0
}

class Version:
    def __init__(self, vers):
        self.components = []
        self.revision = 0

        while vers != None:
            vers = self.make_component(vers)

    def make_component(self, s):
        if len(s) == 0:
            return None

        diglen = 0
        for c in s:
            if not c.isdigit():
                break
            diglen += 1

        # number component
        if diglen > 0:
            self.components.append(int(s[0:diglen]))
            return s[diglen:]

        # known modifier
        for k in mods:
            if s[0:len(k)] == k:
                self.components.append(mods[k])
                return s[len(k):]

        # revision
        if s[0] == "_":
            revlen = 0
            for c in s[1:]:
                if not c.isdigit():
                    break
                revlen += 1
            if revlen > 0:
                self.revision = int(s[1:revlen + 1])
            return s[revlen + 1:]

        # other alphabetics undergo regular comparison
        if s[0].isalpha():
            # like a dot
            self.components.append(0)
            self.components.append(ord(s[0].lower()) - 96)

        return s[1:]

def compare(ver1, ver2):
    ver1 = Version(ver1)
    ver2 = Version(ver2)

    for i in range(max(len(ver1.components), len(ver2.components))):
        if len(ver1.components) > i:
            d1 = ver1.components[i]
        else:
            d1 = 0

        if len(ver2.components) > i:
            d2 = ver2.components[i]
        else:
            d2 = 0

        if d1 != d2:
            return d1 - d2

    return ver1.revision - ver2.revision
