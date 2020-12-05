import re

def parsePassport(p):
    return eval("{'" + p.replace(" ", "', '").replace(":", "':'").replace("\n","', '") + "'}")

def isYrValid(s, mi, ma):
    return len(s) == 4 and mi <= int(s) <= ma

eyeClrs = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
rules = {
    'byr': lambda x : isYrValid(x, 1920, 2002),
    'iyr': lambda x : isYrValid(x, 2010, 2020),
    'eyr': lambda x : isYrValid(x, 2020, 2030),
    'hgt': lambda x : False if re.search("^[0-9]+(cm|in)$", x) is None else
                        150 <= int(x.replace("cm", "")) <= 193 if x.endswith("cm") else
                        59 <= int(x.replace("in", "")) <= 76,
    'hcl': lambda x : re.search("^#[0-9a-f]{6}$", x) is not None,
    'ecl': lambda x : x in eyeClrs,
    'pid': lambda x : re.search("^[0-9]{9}$", x) is not None
}

def isValid(pp, rqd):
    if len(rqd-set(pp.keys())) > 0:
        return False
    return all([rules[r](pp[r]) for r in rules])

expected = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
required = expected - set(['cid'])
passports = [parsePassport(_) for _ in open('input.txt', 'r').read().split('\n\n')]

print(sum([isValid(pp, required) for pp in passports]))
