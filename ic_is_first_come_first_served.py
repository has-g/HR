def is_first_come_first_served_novice(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    myServedOrders = take_out_orders + dine_in_orders
    myServedOrders.sort()

    for x, val in enumerate(served_orders):
        print(served_orders[x])
        if served_orders[x] != myServedOrders[x]:
            return False

    return True



def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    if (len(take_out_orders) + len(dine_in_orders)) != len(served_orders):
        return False

    idx_out = 0
    idx_in = 0

    out_listexists = True
    in_listexists = True

    if len(take_out_orders) == 0: out_listexists = False
    if len(dine_in_orders) == 0: in_listexists = False

    for idx_served in range(len(served_orders)):
        #print("served_order[" + str(idx_served) + "] = " + str(served_orders[idx_served]))
        if (out_listexists == True) and (served_orders[idx_served] == take_out_orders[idx_out]):
            # found the order in take out
            #print("found takeout_order[" + str(idx_out) + "] = " + str(take_out_orders[idx_out]))
            idx_out += 1
            if idx_out == len(take_out_orders): out_listexists = False
        elif (in_listexists == True) and (served_orders[idx_served] == dine_in_orders[idx_in]):
            # found the order in dine in
            #print("found dinein_order[" + str(idx_in) + "] = " + str(dine_in_orders[idx_in]))
            idx_in += 1
            if idx_in == len(dine_in_orders): in_listexists = False
        else:
            return False

    return True


TakeOutOrders = []
DineInOrders = [2, 4, 6]
ServedOrders = [2, 4, 6]

TakeOutOrders = [1, 3, 5]
DineInOrders = [2, 4, 6]
ServedOrders = [1, 2, 4, 6, 5, 3]
#ServedOrders = [1, 2, 3, 4, 5, 6]



print(is_first_come_first_served(TakeOutOrders, DineInOrders, ServedOrders))