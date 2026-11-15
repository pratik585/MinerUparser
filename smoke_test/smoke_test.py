
#%%
from mineru.parser import MinerUParser

#print(type(MinerUParser))

#print(dir(MinerUParser))

#print(help(MinerUParser))


# %%

parser = MinerUParser(
    tier="standard",
    parse_mode="auto",
    image_analysis=True,
    vlm_config=None
)

# %%
result = parser.parse(
    "images/docstructbench_dianzishu_zhongwenzaixian-o.O-61520814.pdf_185.jpg"
)


# %%
from rich import print as rprint

rprint(result)


# %%


from mineru.parser import ParseResult
print(type(ParseResult))
print(dir(ParseResult))
help(ParseResult)


# %%

list_of_parsed_pages = result.export_pages()
rprint(list_of_parsed_pages)



# %%

markdown_of_result = result.markdown()
rprint(markdown_of_result)



# %%

structured_result = result.structured_content()
rprint(structured_result)

# %%

dict_of_result = result.to_dict()
rprint(dict_of_result)

# %%

json_of_result = result.to_json()
rprint(json_of_result)

# %%
