import pandas as pd
def get_services_df(df,services,countries,years):
    services_struct = {service:[] for service in services}
    for i,value in df.iterrows():
        service = value['series']
        if service in services:
            country = value['country']
            if country in countries:
                # add years to a dictionary
                years_dict = {int(year):float(value) 
                              if value != '..' else None
                              for year,value in zip(years,list(df[years].iloc[i]))}
                # add country to the dictionary
                years_dict['country'] = country
                # create a list of dictionaries for services dict
                services_struct[service].append(years_dict)

    service_dfs = {service:None for service in services}
    for key in service_dfs.keys():
        service_df = pd.DataFrame.from_records(services_struct[key]).set_index('country')
        service_df.drop_duplicates()
        service_dfs[key] = service_df
    return service_dfs
