"""

A website domain like "discuss.leetcode.com" consists of various sub_domains.
At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com".
When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received),
followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains.
We would like a list of count-paired domains, (in the same format as the input, and in any order),
that explicitly counts the number of visits to each subdomain.

Example 1:
Input:
["9001 discuss.leetcode.com"]
Output:
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation:
We only have one website domain: "discuss.leetcode.com".
As discussed above,
the subdomain "leetcode.com"
and "com" will also be visited.
So they will all be visited 9001 times.

Example 2:
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation:
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
For the sub_domains, we will visit "mail.com" 900 + 1 = 901 times,
"com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Notes:

The length of cpdomains will not exceed 100.
The length of each domain name will not exceed 100.
Each address will have either 1 or 2 "." characters.
The input count in any count-paired domain will not exceed 10000.
The answer output can be returned in any order.

https://leetcode.com/problems/subdomain-visit-count/

"""


import re


class Solution(object):

    def __init__(self):
        self.sub_domain_dict = dict()

    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        for cpdomain in cpdomains:
            visit_count, sub_domains = self.parse(cpdomain)
            self.countBySubDomain(visit_count, sub_domains)

        return ["{} {}".format(self.sub_domain_dict[sub_domain], sub_domain) for sub_domain in self.sub_domain_dict]

    def parse(self, cpdomain):

        visit_count, domain = cpdomain.split()

        match = re.findall(r'[.]?([\w]+)[.]?', domain)

        parse_result = list(match)

        print(parse_result)

        sub_domains = []
        if len(parse_result) > 2:
            sub_domains.append('.'.join(parse_result))
            sub_domains.append('.'.join(parse_result[1:]))
            sub_domains.append('.'.join(parse_result[2:]))
        elif len(parse_result) > 1:
            sub_domains.append('.'.join(parse_result))
            sub_domains.append('.'.join(parse_result[1:]))
        else:
            sub_domains.append('.'.join(parse_result))

        print(sub_domains)

        return visit_count, sub_domains

    def countBySubDomain(self, visit_count, sub_domains):

        for sub_domain in sub_domains:
            if sub_domain in self.sub_domain_dict:
                self.sub_domain_dict[sub_domain] = self.sub_domain_dict[sub_domain] + int(visit_count)
            else:
                self.sub_domain_dict[sub_domain] = int(visit_count)


def main():
    c = ["9001 discuss.leetcode.com"]
    r = Solution().subdomainVisits(c)
    print(r)

main()
