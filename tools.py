import re
import math


class Calaculation:

    # ==========================================加减乘除=======================================

    def add_sub(self, exp):
        res = 0
        exps = re.findall('[+-]?\d+(?:\.\d+)?', exp)
        for exp in exps:
            res += float(exp)
        return str(res)

    def atom_cal(self, exp):
        if '*' in exp:
            a, b = exp.split('*')
            return str(float(a) * float(b))
        elif '/' in exp:
            a, b = exp.split('/')
            return str(float(a) / float(b))

    def mul_div(self, exp):
        while True:
            ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', exp)
            if ret:
                atom_exp = ret.group()
                res = self.atom_cal(atom_exp)
                exp = exp.replace(atom_exp, res)
            else:
                return exp

    def blend(self, exp):
        if '*' in exp or '/' in exp:
            text = self.mul_div(exp)
            if re.findall('\r*[+-]*', text):
                return self.add_sub(text)
            else:
                return text
        elif '+' in exp or '-' in exp:
            return self.add_sub(exp)
        else:
            return exp

    # ====================================乘方及开方============================================
    def inv(self, exp):
        num, ss = exp.split('**')
        return str(float(num) ** float(ss))

    def squ(self, exp):  # 8//3
        num, ss = exp.split('//')
        result = float(num) ** (1 / float(ss))
        return str(result)

    def inv_squ(self, exp):
        while True:
            ret = re.search('\d+(\.\d+)?\*\*\d+', exp)
            if ret:
                atom_exp = ret.group()
                res = self.inv(atom_exp)
                exp = exp.replace(atom_exp, res)
            else:
                break
        while True:
            ret = re.search('\d+(\.\d+)?//\d+', exp)
            if ret:
                atom_exp = ret.group()
                res = self.squ(atom_exp)
                exp = exp.replace(atom_exp, res)
            else:
                break
        return exp

    # =======================================括号优先级相关=====================================

    def bra(self, exp):
        while True:
            ret = re.search('\{.*?\w?\}', exp)
            if ret:
                atom_exp = ret.group()
                res = self.bra_main(atom_exp)
                exp = exp.replace(atom_exp, res)
            else:
                return exp

    def big_bra(self, exp):
        while True:
            ret = re.search('\[.*?\w?\]', exp)
            if ret:
                atom_ret = ret.group()
                res1 = self.bra(atom_ret)
                res2 = self.bra_main(res1)
                exp = exp.replace(atom_ret, res2)
            else:
                return exp

    # =========================================三角函数=========================================

    def sin(self, exp):
        while True:
            ret = re.search('sin\(\d+(\.\d+)?[+\-*/]?(\d+(\.\d+)?\))?', exp)
            if ret:
                atom = ret.group()
                res = str(
                    math.sin(
                        float(
                            self.blend(
                                atom.replace('sin(', '')
                            )
                        )
                    )
                )
                exp = exp.replace(atom, res)
            else:
                return exp

    def cos(self, exp):
        while True:
            ret = re.search('cos\(\d+(\.\d+)?[+\-*/]?(\d+(\.\d+)?\))?', exp)
            if ret:
                atom = ret.group()
                res = str(
                    math.cos(
                        float(
                            self.blend(
                                atom.replace('cos(', '')
                            )
                        )
                    )
                )
                exp = exp.replace(atom, res)
            else:
                return exp

    def tan(self, exp):
        while True:
            ret = re.search('tan\(\d+(\.\d+)?[+\-*/]?(\d+(\.\d+)?\))?', exp)
            if ret:
                atom = ret.group()
                res = str(
                    math.tan(
                        float(
                            self.blend(
                                atom.replace('tan(', '')
                            )
                        )
                    )
                )
                exp = exp.replace(atom, res)
            else:
                break
        return exp

    def arcsin(self, exp):
        while True:
            ret = re.search('arcsin\(\d+(\.\d+)?[+\-*/]?(\d+(\.\d+)?\))?', exp)
            if ret:
                atom = ret.group()
                res = str(
                    math.asin(
                        float(
                            self.blend(
                                atom.replace('arcsin(', '')
                            )
                        )
                    )
                )
                exp = exp.replace(atom, res)
            else:
                return exp

    def arccos(self, exp):
        while True:
            ret = re.search('arccos\(\d+(\.\d+)?[+\-*/]?(\d+(\.\d+)?\))?', exp)
            if ret:
                atom = ret.group()
                res = str(
                    math.acos(
                        float(
                            self.blend(
                                atom.replace('arccos(', '')
                            )
                        )
                    )
                )
                exp = exp.replace(atom, res)
            else:
                return exp

    def arctan(self, exp):
        while True:
            ret = re.search('arctan\(\d+(\.\d+)?[+\-*/]?(\d+(\.\d+)?\))?', exp)
            if ret:
                atom = ret.group()
                res = str(
                    math.atan(
                        float(
                            self.blend(
                                atom.replace('arctan(', '')
                            )
                        )
                    )
                )
                exp = exp.replace(atom, res)
            else:
                break
        return exp

    def sct(self, exp):
        exp = self.arcsin(exp)
        exp = self.arccos(exp)
        exp = self.arctan(exp)
        exp = self.sin(exp)
        exp = self.cos(exp)
        exp = self.tan(exp)

        return exp.replace(')', '')
        #return exp

    #  =====================================总运行函数==========================================

    def bra_main(self, exp):
        exp = self.inv_squ(exp)
        exp = self.sct(exp)
        exp = self.blend(exp)
        return exp

    def main(self,exp):
        res = self.big_bra(exp)
        return self.bra_main(res)
