# Check If a String Can Break Another String
# User Accepted:1106
# User Tried:1281
# Total Accepted:1112
# Total Submissions:1633
# Difficulty:Medium
# Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).
#
# A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        sum1 = 0
        sum2 = 0
        ss1 = sorted(s1)
        ss2 = sorted(s2)

        for i, s in enumerate(ss1):
            if s >= ss2[i]:
                sum1 += 1
            if s <= ss2[i]:
                sum2 += 1

        return sum1 == len(s1) or sum2 == len(s1)


s1 = "tzglpoqbmrpnljswforeqnpkzicujvqczpcsfumcpswklsbnyoqsqmlmxmftljzzymtrpwufpsxosgzqjjopryeyogwmkxujfbokjlgqoialugpoeedkdltrkrdikezrlyflegktbjlwqalwvltutlhtgpieuxsxahgvtggmtcsahucnbwpyzxqgcqmrjlcwgsbetlvndqoydezfqanmypezosdtkhsdqbidnpebxjsprgoaixxxbeazjnsfebgcffekprqloqohtkprrmiewtovirltqiqlxneytqbjoboscerfzvemvhrmthjuuxrhfwetrnbzmxagrpidltsfuzifrxfvxjrwxqpjjglsqpizqzuwiffofgfvegbevpoycmrswbtaotodzvoxnsokkbydxzcitzzlbsyjihlhmgfdbuvofaewxawzpvraboqxrhhiyknqhakrojnhjgmfzgadcjnxfnngfqqnntzjsslcgmtoxgqxcvkwglvbovkcvbptjkrbsdlnrtqqwlhjutngwzhwwjmwvewqqkutzxjkftijnfqwccsdyabokviehrcxpeibdyckitsptndbkresokltoawxukvlyipgifjpbjdgopbcginihbpgdcqswonjccolxalhskkvmwduhjzldatxfpevlorrwfkpponojfnfnklekexadynykwaqtpoiggagxkrxspqhbiimaeylxpvvnesqwnuagzjloszrwiaftkezfvstkhyiskjmwqjiazoulhwivfnvskzkmfmiiiljvevprusklydwciuugotxuwygxmuomomaqhvyaynt"
s2 = "pnovjpkvkozvgobaaxhzuqbvfhdgejtlwllqhwplgfygjhyebqvljuyzudecwnyxhqircaavqgcrrocjngthjxfcqtsuvrlcdozjzpzlloejtpnsqvfwdypndzsizxxgljytzitpfjaoimsfopzewiecnpevrjsxjxzlmcaikbmrinfmaktwxrtznuusckorkphoygsfndqtwdiprcgpmrpesilymtuqnainifhmfrqicmlrjyxvfgmbnnctjfndalcbvgaicrkvaetqgrwagyhvznoyqqrrokmdwtjpzadlsinnknpdpwxxzmsomwpdgwkqnoyhosjnfdcabioeomkhcckboxjbqyzddgnngnykzcbvzbsouordibkzdajyvghtvegmwewgnjjlotqatzecmzrmhmvujetabnuyczkknlmggnfcfvlsxabazvaylssqbmynsqmsqnofxbeyavvkngweupgnhgfmwrutruabeueobvkffnopaxixzgpnqyhvkhjxdifaxnaenemfowrikyxvscnyrtrxlrghxotuaorxlmkgfredzvwabclmhtnijeiqdjjugsuhzwtjwiitymcfijkimhfrbskvovsoeoxfxydkusbyqguxtsvbcegdvqzbdjilotpkildckpayaguqcyfjslfvrpwlrhhixxetcoalgpwrhzbuczycjjufjbminigywmedzcgigvsauiimyxuoctrisaftdaecigaqjlrvrlaxjlhmiatkcxsapxrnuwxqsenlicqiqknuksuocibeuhqwawqhbaotqgivnbutxidhgchgtsomfgpz"

s1 = "abc"
s2 = "abg"

foo = Solution()
print(foo.checkIfCanBreak(s1, s2))
