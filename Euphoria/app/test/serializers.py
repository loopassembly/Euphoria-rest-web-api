
from pyexpat import model
from django.http import response
from rest_framework import serializers
from rest_framework.response import Response
from django.http import request

from .models import User,Menu,cov_data,cov_name

class MenuSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
       model = Menu
       fields = ("id","item_name","item_image","cost","bake_time","status",'food_type',"menu")
       extra_kwargs = {
            'item_name': {'validators': []},
        }
       read_only_fields = ('menu',)

class UserSerializer(serializers.ModelSerializer):
    items = MenuSerializer(many=True)
    
    class Meta:
        model = User
        fields = ("id","email","name","password",'items')
    #    extra_Kwargs = {
    #         'password':{
    #             'write_only': True,
    #             'style':{'input_type':'password'}
    #         }
    #    }
        extra_kwargs = {'password':
             {'write_only':True,
                'style':{'input_type':'password'}
                }
            }
        
    
    def create(self, validated_data):
        '''create and return a new user'''
        items_data = validated_data.pop('items')
        # menu =User.objects.create(**validated_data)
        menu = User.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
            password = validated_data['password']

        )
        
        for item in items_data:
            Menu.objects.create(**item,menu=menu)

      
        
        
    
        return menu

    def update(self, instance, validated_data):
       
        items = validated_data.pop('items')
        print(items)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        res=False
        keep_items = []
        for choice in items:
            
            val_data_len=len(choice)
            
            if "id" in choice.keys():
                # print("id")
                if Menu.objects.filter(id=choice["id"]).exists():
                    c = Menu.objects.get(id=choice["id"])
                    c.item_name = choice.get('item_name', c.cost)
                    c.cost = choice.get('cost', c.item_name)
                    c.bake_time = choice.get('bake_time', c.bake_time)
                    c.status = choice.get('status', c.status)

                    c.save()
                    keep_items.append(c.id)
                else:
                    continue
            else:
                # model_val=Menu.objects.values_list('item_name',"menu")
                # user_val=choice["item_name"]
                # print(user_val)
                # print(model_val)
                # test =items
                # print(test)
                # if user_val not in  model_val:
                if not  Menu.objects.filter(item_name=choice['item_name'], menu=instance).exists():

                    c = Menu.objects.create(**choice, menu=instance)
                    keep_items.append(c.id) 
                    
                            
                else:
                    # print(Menu.objects.filter(id="").exists())
                    raise serializers.ValidationError("item with this name already exists")
                    
                    
 
       
        
             
            if "id" in choice.keys() and val_data_len==1:
                    print("id")
                    if Menu.objects.filter(id=choice["id"]).exists():
                        print(Menu.objects.filter(id=choice["id"]),"data")
                        c = Menu.objects.get(id=choice["id"])
                        print(c.id)
                        for i in Menu.objects.all():
                            
                            if i.id==c.id:
                                
                                i.delete()

        return instance
    
    


class Cov_data_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
       model = cov_data
       fields = ("id","date","time","temp",'cov_name')
    

class cov_name_Serializer(serializers.ModelSerializer):
    cov_data = Cov_data_Serializer(many=True)
    
    class Meta:
        model = cov_name
        fields = ("id","name","number",'name_image','alert',"cov_data")


    def create(self, validated_data):
        '''create and return a new user'''
        items_data = validated_data.pop('cov_data')
        cov_post = cov_name.objects.create(**validated_data)
        for item in items_data:
            cov_data.objects.create(**item,cov_name=cov_name)
        
        return cov_post

    def update(self, instance, validated_data):
       
        # items = validated_data.pop('items')
        cov_data_feed = validated_data.pop('cov_data')
        instance.name = validated_data.get("name", instance.name)
        instance.number = validated_data.get("number", instance.number)
        instance.name_image = validated_data.get("name_image", instance.name_image)
        instance.alert = validated_data.get("alert", instance.alert)
       
        instance.save()
        res=False
        keep_items = []
        for data in cov_data_feed:
            
            val_data_len=len(data)
            
            if "id" in data.keys():
                # print("id")
                if cov_data.objects.filter(id=data["id"]).exists():
                    c = cov_data.objects.get(id=data["id"])
                    c.temp = data.get('temp', c.temp)
                    

                    c.save()
                    keep_items.append(c.id)
                else:
                    continue
            else:
               
               c = cov_data.objects.create(**data, cov_name=instance)
               keep_items.append(c.id) 
                    
                            
               
 
       
        
             
            # if "id" in choice.keys() and val_data_len==1:
            #         print("id")
            #         if Menu.objects.filter(id=choice["id"]).exists():
            #             print(Menu.objects.filter(id=choice["id"]),"data")
            #             c = Menu.objects.get(id=choice["id"])
            #             print(c.id)
            #             for i in Menu.objects.all():
                            
            #                 if i.id==c.id:
                                
            #                     i.delete()

        return instance
