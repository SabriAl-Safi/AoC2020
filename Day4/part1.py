def parsePassport(p):
    return eval("{'" + p.replace(" ", "', '").replace(":", "':'").replace("\n","', '") + "'}")

def isValid(pp, rqd):
    return len(rqd-set(pp.keys())) == 0

expected = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
required = expected - set(['cid'])
passports = [parsePassport(_) for _ in open('input.txt', 'r').read().split('\n\n')]

print(sum([isValid(pp, required) for pp in passports]))
