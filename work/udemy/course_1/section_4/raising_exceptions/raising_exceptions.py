def ProcessInvoice(netto, brutto):
    if netto >= brutto:
        raise ValueError("Netto should be lower or equal to brutto")
    else:
        print("Processing invoice: nett={} brutto={}".format(netto, brutto))


def EndOfMonth():
    netto = 1230
    brutto = 10000

    try:
        ProcessInvoice(netto, brutto)
    except ValueError as e:
        print("The values on invoice are incorrect: {}".format(e))
        raise ValueError('Error when processing invoices') from e
    except Exception as e:
        print("Error processing invoice: {}".format(e))
        raise Exception("General error when processing invoices")


EndOfMonth()