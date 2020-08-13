class math():
    def gcd(self, a, b):
        """ 求两个数字的最大公约数
        Args:
            a : 第一个数字
            b : 第二个数字
        Rtns:
            c : 最大公约数
        Raises:
            TyepError : 防止输入错误变量类型
        """
        if type(a) != int or type(b) != int:
            raise TypeError("type int needed in gcd functions!")
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def ext_euclid(self, a, b):
        """ 扩展欧几里得算法
        Args:
            a : 第一个数字
            b : 第二个数字
        Returns:
            rtn1 : 最大公约数
            rtn2 : x
            rtn3 : y
        Raises:
            TyepError : 防止输入错误变量类
        """
        if type(a) != int or type(b) != int:
            raise TypeError("type int needed in gcd functions!")
        old_s, s = 1, 0
        old_t, t = 0, 1
        old_r, r = a, b
        if b == 0:
            return 1, 0, a
        else:
            while(r != 0):
                q = old_r//r
                old_r, r = r, old_r-q*r
                old_s, s = s, old_s-q*s
                old_t, t = t, old_t-q*t
        return old_s, old_t, old_r

    def exp_mode(self, base, exponent, n):
        """ 蒙哥马利算法：计算超大整数的超大幂
        Args: 
            base : 超大整数
            exponent : 超大幂次
        Returns:
        """
        bin_array = bin(exponent)[2:][::-1]
        r = len(bin_array)
        base_array = []

        pre_base = base
        base_array.append(pre_base)

        for _ in range(r - 1):
            next_base = (pre_base * pre_base) % n
            base_array.append(next_base)
            pre_base = next_base

        a_w_b = self.__multi(base_array, bin_array, n)
        return a_w_b % n

    def __multi(self, array, bin_array, n):
        result = 1
        for index in range(len(array)):
            a = array[index]
            if not int(bin_array[index]):
                continue
            result *= a
            result = result % n
        return result


class rsa():
    def __init__(self):
        self.math = math()

    def gen_key(self, p, q):
        n = p * q
        fy = (p - 1) * (q - 1)      # 计算与n互质的整数个数 欧拉函数
        e = 65537                    # 选取e   一般选取65537
        # generate d
        a = e
        b = fy
        r, x, y = self.math.ext_euclid(a, b)
        # 计算出的x不能是负数，如果是负数，说明p、q、e选取失败，不过可以把x加上fy，使x为正数，才能计算。
        if x < 0:
            x = x + fy
        d = x
        # 返回：   公钥     私钥
        return (n, e), (n, d)
    