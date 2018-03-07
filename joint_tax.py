def joint_assessment(a, b):
    # a = int(input('Enter Wife Personal Income: '))
    # b = int(input('Enter Husband Personal Income: '))
    testForDataType = 0

    if type(a) != type(testForDataType) and type(b) != type(testForDataType):
        print('Error input!\n')
        return 'Error input!'
    elif a and b >= 0:
        print('Wife & Husband personal income: ', a, '&', b)

        c = a * 0.05  # Wife Net Total Income (After MPF deduction)
        d = b * 0.05  # Husband Net Total Income (After MPF deduction)

        e = c  # Wife Net Chargeable Income (After  deduction Allowance)
        f = d  # Husband Net Chargeable Income (After  deduction Allowance)

        g = e  # Wife Tax
        h = f  # Husband Tax

        i = g  # Wife Tax Payable
        j = h  # Husband Tax Payable

        k = 0  # Joint Tax
        l = 0  # Joint Tax Payable

        # Wife Net Total Income (After MPF deduction)
        if c >= 15000:
            c = a - 15000
        else:
            c = a * 0.95
        print('Wife Net Total Income (After MPF deduction): ', c)


        # Husband Net Total Income (After MPF Deduction)
        if d >= 15000:
            d = b - 15000
        else:
            d = b * 0.95
        print('Husband Net Total Income (After MPF deduction): ', d)


        # Wife Net Chargeable Income (After  deduction Allowance)
        if c >= 132000:
            e = c - 132000
        else:
            e = 0
        print('Wife Net Chargeable Income (After  deduction Allowance): ', e)


        # Husband Net Chargeable Income (After  deduction Allowance)
        if d >= 132000:
            f = d - 132000
        else:
            f = 0
        print('Husband Net Chargeable Income (After  deduction Allowance): ', f)


        # Wife Tax
        if e >= 135000:
            g = 9450 + (e - 135000) * 0.17
        elif e >= 90000:
            g = 4050 + (e - 90000) * 0.17
        elif e >= 45000:
            g = 900 + (e - 45000) * 0.17
        else:
            g = e * 0.17
        print('Wife Tax: ', g)


        # Husband Tax
        if f >= 135000:
            h = 9450 + (f - 135000) * 0.17
        elif f >= 90000:
            h = 4050 + (f - 90000) * 0.17
        elif f >= 45000:
            h = 900 + (f - 45000) * 0.17
        else:
            h = f * 0.17
        print('Husband Tax: ', h)


        # Wife Tax Payable
        if g * 0.75 >= 20000:
            i = g - 20000
        else:
            i = g - g * 0.75
        print('Wife Tax Payable: ', i)


        # Husband Tax Payable
        if h * 0.75 >= 20000:
            j = h - 20000
        else:
            j = h - h * 0.75
        print('Wife Tax Payable: ', j)

        # Joint Tax
        def calK():
            if c + d - 264000 >= 135000:
                k = 9450 + (c + d - 399000) * 0.17
            elif c + d - 264000 >= 90000:
                k = 4050 + (c + d - 354000) * 0.17
            elif c + d - 264000 >= 45000:
                k = 900 + (c + d - 309000) * 0.17
            else:
                k = (c + d - 264000) * 0.17
            return k

        if calK() <= 0:
            k = 0
        elif c + d - 264000 >= 135000:
            k = 9450 + (c + d - 399000) * 0.17
        elif c + d - 264000 >= 90000:
            k = 4050 + (c + d - 354000) * 0.17
        elif c + d - 264000 >= 45000:
            k = 900 + (c + d - 309000) * 0.17
        else:
            k = (c + d - 264000) * 0.17
        print('Joint Tax: ', k)

        # Joint Tax Payable
        if k * 0.75 >= 20000:
            l = k - 20000
        else:
            l = k - k * 0.75
        print('Joint Tax Payable: ', l)

        # Joint Assessment Recommended (Y/N)
        if l >= i + j:
            print('Joint Assessment Recommended: N\n')
        else:
            print('Joint Assessment Recommended: Y\n')

        return l
    else:
        print('Error input!\n')
        return 'Error input!'





