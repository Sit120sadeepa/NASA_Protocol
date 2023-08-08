/*	This is a sample selectcla.c file that selects the first
 *	bssp outduct it finds if the service number in the outbound
 *	bundle's destination EID is 99; otherwise it selects the
 *	first ltp or tcp outduct it finds.
 *
 *	This very simply outduct selection logic by no means exhausts
 *	the capabilities of this feature.  Outduct selection logic
 *	can be arbitrarily complex to meet mission requirements.  For
 *	example, outducts might be selected on the basis of bundle
 *	data label, payload size, or even non-bundle state information
 *	such as calendar date.						*/

	if (bundle->destination.ssp.ipn.serviceNbr == 99)
	{
		if (strcmp(protocol->name, "bssp") == 0)
		{
			return 1;
		}

		continue;
	}

	if (strcmp(protocol->name, "ltp") == 0)
	{
		return 1;
	}

	if (strcmp(protocol->name, "tcp") == 0)
	{
		return 1;
	}
