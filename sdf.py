from gempyp.libs.enums.status import status
import json
class beforeAfter:
    def after_(self,obj):
        obj.keys = ["ID","Name"]
        return obj
    def before_(self,obj):
        value_dict = obj.value_df
        value_dict.rename(columns = {'REASON OF FAILURE':'rof'}, inplace = True)
        obj.value_df=value_dict
        return obj
    