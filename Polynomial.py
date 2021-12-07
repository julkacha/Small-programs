import copy

class Polynomial:

    __slots__ = ['__c', 'n']

    def __init__(self, *c):
        if isinstance(c[0], Polynomial):
            self.copy(c)
        else:
            self.original(c)

    def original(self, c):
        if isinstance(c[0], list):
            self.__c = list(c[0])
        else:
            self.__c = list(c)

        self.n = []
        n = len(self.__c) - 1
        for i in range(len(self.__c)):
            self.n.append(n)
            n -= 1

    def copy(self, other):
        orig = other[0]
        self.__c = copy.deepcopy(orig.__c) ##
        self.n = copy.deepcopy(orig.n)

    def __str__(self):
        out = ""
        for i in range(len(self.__c)):
            ci = self.__c[i]
            n = self.n[i]
            if ci == 0 and i != len(self.__c)-1:
                continue
            else:
                if ci < 0 and i != 0:
                    ci *= -1
                elif ci < 0 and i == 0:
                    ci *= -1
                    out += "- "

                if i < len(self.__c)-1 and self.__c[i+1] < 0:
                    sg = "-"
                else:
                    sg = "+"

                if n == 0:
                    out += str(ci)
                elif n == 1:
                    out += str(ci) + "*x" + " " + sg + " "
                else:
                    out += str(ci) + "*x^" + str(n) + " " + sg + " "
        return out

    def __iadd__(self, other):
        for i in range(len(self.__c)):
            for j in range(len(other.__c)):
                if self.n[i] == other.n[j]:
                    self.__c[i] += other.__c[j]

        for i in range(len(other.n)):
            if other.n[i] not in self.n:
                self.__c.insert(i, other.__c[i])
                self.n.insert(i, other.n[i])
        return self

    def __isub__(self, other):
        for i in range(len(self.__c)):
            for j in range(len(other.__c)):
                if self.n[i] == other.n[j]:
                    self.__c[i] -= other.__c[j]

        for i in range(len(other.n)):
            if other.n[i] not in self.n:
                self.__c.insert(i, other.__c[i])
                self.__c[i] *= -1
                self.n.insert(i, other.n[i])
        return self

    def __imul__(self, other):
        temp_c = []
        temp_n = []
        for i in range(len(self.__c)):
            temp_c.append([])
            temp_n.append([])
            for j in range(len(other.__c)):
                temp_c[i].append(self.__c[i] * other.__c[j])
                temp_n[i].append(self.n[i] + other.n[j])

        for k in range(len(temp_n)):
            ln = temp_n[k]
            lc = temp_c[k]
            for i in range(len(ln)-1):
                if ln[i] != ln[i+1]+1:
                    lc.insert(i+1, 0)
                    ln.insert(i+1, ln[i]-1)
            while ln[len(ln)-1] != 0:
                lc.append(0)
                ln.append(ln[len(ln)-1]-1)
            temp_c[k] = Polynomial(lc)
            if k > 0:
                temp_c[k] += temp_c[k-1]
        self.__c = temp_c[len(temp_c)-1].__c ##
        self.n = temp_c[len(temp_c)-1].n
        return self

    def __add__(self, other):
        newpol = Polynomial(self.__c)
        for i in range(len(newpol.__c)):
            for j in range(len(other.__c)):
                if newpol.n[i] == other.n[j]:
                    newpol.__c[i] += other.__c[j]

        for i in range(len(other.n)):
            if other.n[i] not in newpol.n:
                newpol.__c.insert(i, other.__c[i])
                newpol.n.insert(i, other.n[i])
        return newpol

    def __sub__(self, other):
        newpol = Polynomial(self.__c)
        for i in range(len(newpol.__c)):
            for j in range(len(other.__c)):
                if newpol.n[i] == other.n[j]:
                    newpol.__c[i] -= other.__c[j]

        for i in range(len(other.n)):
            if other.n[i] not in newpol.n:
                newpol.__c.insert(i, other.__c[i])
                newpol.__c[i] *= -1
                newpol.n.insert(i, other.n[i])
        return newpol

    def __mul__(self, other):
        newpol = Polynomial(self.__c)
        temp_c = []
        temp_n = []
        for i in range(len(newpol.__c)):
            temp_c.append([])
            temp_n.append([])
            for j in range(len(other.__c)):
                temp_c[i].append(newpol.__c[i] * other.__c[j])
                temp_n[i].append(newpol.n[i] + other.n[j])

        for k in range(len(temp_n)):
            ln = temp_n[k]
            lc = temp_c[k]
            for i in range(len(ln)-1):
                if ln[i] != ln[i+1]+1:
                    lc.insert(i+1, 0)
                    ln.insert(i+1, ln[i]-1)
            while ln[len(ln)-1] != 0:
                lc.append(0)
                ln.append(ln[len(ln)-1]-1)
            temp_c[k] = Polynomial(lc)
            if k > 0:
                temp_c[k] += temp_c[k-1]
        newpol.__c = temp_c[len(temp_c)-1].__c ##
        newpol.n = temp_c[len(temp_c)-1].n
        return newpol

    def __call__(self, x = 0):
        val = 0
        for i in range(len(self.__c)):
            val += self.__c[i] * x ** self.n[i]
        return val

    def differentiate(self):
        dif = Polynomial(self.__c)
        for i in range(len(dif.__c)):
            dif.__c[i] *= dif.n[i]
            if dif.n[i] > 0:
                dif.n[i] -= 1
            else:
                del dif.n[i]
                del dif.__c[i]
        return dif

    def integrate(self):
        ing = Polynomial(self.__c)
        for i in range(len(ing.__c)):
            ing.n[i] += 1
            ing.__c[i] /= ing.n[i]
        ing.n.append(0)
        ing.__c.append(0)
        print("integrate method: 0 at the end represents a constant")
        return ing
    
    @property
    def coefficients(self): return copy.deepcopy(self.__c[::-1])


if __name__ == "__main__":
    w1 = Polynomial([1, 2, 3, 5])
    w2 = Polynomial(5, 2, 1)
    w3 = w1 + w2
    print(w3)
    print(w1)
    w1 *= w3
    print(w1)