"""
You are responsible for collecting signatures from all tenants of a certain building.
For each tenant, you know a period of time when he or she is at home. You would like
to collect all signatures by visiting the building as few times as possible.
"""

n = int(input())
tenants = [tuple(map(int, input().split())) for _ in range(n)]

def is_tenant_available(tenant, time):
    return tenant[0] <= time <= tenant[1]


def greedy_strategy(tenants):
    right_points = sorted([y for x, y in tenants])
    signatures_left = 0
    point = right_points.pop(0)
    tenant_visited = set()
    for index in range(len(tenants)):
        tenant = tenants[index]
        if is_tenant_available(tenant, point):
            pass
    return right_points


print(greedy_strategy(tenants))