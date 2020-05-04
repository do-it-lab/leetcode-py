"""

You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words
exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""


class Solution(object):
    def findSubstring(self, s, words):

        indices = []

        whole_string_size = len(s)
        window_size = len("".join(words))
        shift_size = 1
        index = 0

        while index + window_size <= whole_string_size:
            substring = s[index: window_size+index]
            match, remain_string = self.match(substring, words)
            if match:
                indices.append(index)

            #print(index, substring, words, match, remain_string)
            index = index + shift_size

        return indices

    def match(self, substring, words):

        copied_words = list(words)
        substring_size = len(substring)
        slice_size = len(copied_words[0])
        left = 0
        remain_string = ''
        while left + slice_size <= substring_size:
            word = substring[left: left+slice_size]
            if word not in copied_words:
                remain_string = remain_string + word

            else:
                copied_words.remove(word)
            left = left + slice_size

        return len(remain_string) == 0, remain_string


class SolutionWrongAnswer(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]

        "wordgoodgoodgoodbestword"
        ["word","good","best","good"]

        """

        window_size = len("".join(words))
        slice_size = len(words[0])

        offset = 0

        result_offsets = []
        while True:

            # init
            sub_string = s[offset:offset + window_size]

            # exit condition
            if len(sub_string) < window_size:
                break

            sliced_words = self.slice_by_size(sub_string, slice_size)
            if self.validate(sliced_words, words):
                result_offsets.append(offset)

            # offset control
            offset = offset + slice_size

        return result_offsets

    def slice_by_size(self, sub_string, size):

        return [sub_string[i:i + size] for i in range(0, len(sub_string), size)]

    def validate(self, sliced_words, words):

        dup = set()
        for word in sliced_words:
            if word not in words:
                return False

            elif word in dup:
                return False

            else:
                dup.add(word)

        return True


def main():

    #s = "barfoothefoobarman"
    #words = ["foo", "bar"]

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]

    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]

    s ="syvsjefxttjyqamnntfucrpeoculzlzsjukuarrtmbuddiqsbxmdodjdffqfrpzcjjxmcofprzuwikpjhbpxhycmettxiuzufwginlxgnrdxduimxxjewmtchmzpjyjovrwifvqsmtprpxdnxprtdkvkzuziulwpcvzhqqbflswbscqprhiuufetbfdvsznvwoengisuaqvssnhjurfoyljbrmzjomgkcnxjvrdviaqanzmjtrardjvwwufmgowibwtwnwtxwjyljmvcfvvigqgekmqscpddlwbatuyreyfpkarpxoadhgiruamyppbancdgxbadbfsnhleezejgntajumijdlmqqpzpqbstgkgpxkvwpefeyfpstzdwlpodenswokpwwvltgirxpydndshyumwhclkiycfpoulmszhyjyxyzancuwdojzxlkhtllaczxpnpqupavmyuomykibbrbyengaarcctzsgoibdkyrjsfvqqfurzvpfkxfnripkjjqyutdervnlckcuqylrtdwfccstmkfxtwvprbulwjwawavoyiftnbbqftltfrrbpmqgpmtlysouujivrpqfqrxwnirszitoxmxmyqaykosfxcaqtqvkksizbzrcknrhbotbgvarjuyizyzsquccpmbsovuyklflbamiwobhjzqkzpcrlhuctxuhsrhcempgpeqlsrudsknrbskpzerscocwfjbjyqpnuhapauushklicwxdcpxgdzfklgtlwlatsaktwgndqzouxlxbcxihwprjvlwtwwoqyyjvhzaxaouxataeqkmpzdauqxomtcfudopkprjpgdoizpmpzyezehvuejhzomtrckbsckjiqyspnegofnnjujdaukziytbddcxhpgphghytogkttxcpifpdsrnsmpxrtuzkdqtlathoarhvollzqcektrdficxezwocmkpmdwcdnlzcwmdpohziaepjhmngkdkznznrwqwlbvnahspwzqgaxvlgkyoudatrzhkxzgjceycnttlskruhpfpzfdtldpceyoexwpbcpeqixbbjtxskfhjkkcvntzsrpyomnqocwglviofdlznqhwdrayhuablrzcdmuuosabnkpunbuatbywubxdvzeiqfmuriqiasjodzkqcetvhtueurhpqoaitmcnvuxxngnqhyiledhoxdsrubjmpjujxzysvvsidfaldlyiofylkqferoshxnsuospjnhusmwfsjecylalwqqajevsdkmayerjtyfmmcrglviljkxfcpfmwcgzmtzmzqwtqdhffaltywghgfmlvtxrwdskyuxymvtfyakgaxbavhhentpknobltvvspsscpljontwpsxqoexuttjdizgtscqmtlexapgqcbmsulkkqhelappiovdizuvvfzsfrbyvckpywzkojqzjhquxmxgnrdiyedgxgetkqklomvcvoeevuatiybwregsilyirebcunnjzknuytbuobpwbquvwdngonogrrknfzyejobihcevftuhloehrtnggcoztamaznfibgqikweppayaochivxqdbgcwgrxfeenfmgnwctnstmukqeuobkreqwawnxbtdqypwnlbjztenpodtitwulakhbiwajpecptyehzniusvmiaftucnhe"
    words = ["qbflswbscqprhiuufetbfd", "vsznvwoengisuaqvssnhju", "rfoyljbrmzjomgkcnxjvrd", "viaqanzmjtrardjvwwufmg",
     "owibwtwnwtxwjyljmvcfvv", "igqgekmqscpddlwbatuyre", "yfpkarpxoadhgiruamyppb", "ancdgxbadbfsnhleezejgn",
     "tajumijdlmqqpzpqbstgkg", "pxkvwpefeyfpstzdwlpode", "nswokpwwvltgirxpydndsh", "yumwhclkiycfpoulmszhyj",
     "yxyzancuwdojzxlkhtllac", "zxpnpqupavmyuomykibbrb", "yengaarcctzsgoibdkyrjs", "fvqqfurzvpfkxfnripkjjq",
     "yutdervnlckcuqylrtdwfc", "cstmkfxtwvprbulwjwawav", "oyiftnbbqftltfrrbpmqgp", "mtlysouujivrpqfqrxwnir"]

    indices = Solution().findSubstring(s=s, words=words)
    print(indices)

main()