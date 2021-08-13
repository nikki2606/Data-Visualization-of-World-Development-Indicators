# Below a dictionary of dictionary is created which maps a service with its countries for which 
# each country is further mapped with values for all the years 
def get_services_dict(df,services,countries,years):
    services_dict = {service:{} for service in services}
    for i,value in df.iterrows():
        service = value['series']
        if service in services:
            country = value['country']
            if country in countries:
                services_dict[service][country] = {year:value 
                                                   for year,value 
                                                   in zip(years,list(df[years].iloc[i]))}
    return services_dict
