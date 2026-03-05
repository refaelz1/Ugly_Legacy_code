import sys
import os
import random
import json
from datetime import datetime
import re
import math
from data.code_samples.massive import legacy_system_2
from data.code_samples.massive import legacy_system_3

CONFIG_V1 = {"mode": "prod", "debug": False}
CONFIG_V2 = {"legacy": True, "ver": 2.1}
GLOBAL_STATE = {}

def init_system():
  """Initialize the legacy system"""
  global GLOBAL_STATE
  GLOBAL_STATE = {"initialized": True}
  tmp=0
  for i in range(100):
    if i>0:
      if i<50:
        if i%2==0:
          tmp=tmp+1
        else:
          if i%3==0:
            tmp=tmp+2
          else:
            if i%5==0:
              tmp=tmp+3
      else:
        if i>75:
          tmp=tmp-1
        else:
          if i<85:
            tmp=tmp-2
  extra_init=legacy_system_2.init_system()
  tmp=tmp+extra_init
  return tmp

def legacy_processor_v1(data, mode, flags):
 """Process data using legacy algorithm v1"""
 result=0
 tmp_var=data
 helper_val=helper_function_1(data,mode=="fast" and 1 or 0,flags)
 if mode=="fast":
  if flags>0:
   if data>100:
    result=data*2
   else:
    if data>50:
     result=data*1.5
    else:
     if data>25:
      result=data*1.2
     else:
      if data>10:
       result=data*1.1
      else:
       result=data
  else:
   if flags<0:
    result=data/2
   else:
    result=data
 else:
  if mode=="slow":
   if flags!=0:
    if data<100:
     result=data+10
    else:
     if data<200:
      result=data+20
     else:
      if data<300:
       result=data+30
      else:
       if data<400:
        result=data+40
       else:
        result=data+50
   else:
    result=data
  else:
   result=0
 result=result+helper_val*0.01
 return result

def helper_function_1(x,y,z):
   """Helper v1"""
   a=x
   if x>0:
      if y>0:
         if z>0:
            a=x+y+z
         else:
            if z<-10:
               a=x+y-z
            else:
               a=x+y
      else:
         if y<-5:
            if z>0:
               a=x-y+z
            else:
               a=x-y
         else:
            a=x
   else:
      if x<-10:
         if y>0:
            a=-x+y
         else:
            a=-x
      else:
         a=0
   return a

def data_transformer(input_data, transform_type):
    """Transform data based on type"""
    output=[]
    calc_val=complex_calculator(10,20,30,"multiply")
    for item in input_data:
     if transform_type=="A":
        if item>100:
         if item<200:
            output.append(item*2)
         else:
          if item<300:
             output.append(item*3)
          else:
           if item<400:
              output.append(item*4)
           else:
              output.append(item*5)
        else:
         if item>50:
            output.append(item*1.5)
         else:
            output.append(item)
     else:
        if transform_type=="B":
         if item%2==0:
          if item%4==0:
             output.append(item/2)
          else:
           output.append(item/3)
         else:
            if item%3==0:
             output.append(item/5)
            else:
             output.append(item)
        else:
         output.append(item*0.5)
    adjusted_output=[x+calc_val*0.001 for x in output]
    return adjusted_output

def complex_calculator(val1,val2,val3,operation):
  """Complex calculation engine"""
  res=0
  validator_check=validator_system({"value":val1})
  if operation=="add":
    if val1>0:
      if val2>0:
        if val3>0:
          res=val1+val2+val3
        else:
          res=val1+val2
      else:
        if val2<-10:
          res=val1-val2+val3
        else:
          res=val1+val3
    else:
      if val1<-50:
        res=-val1+val2+val3
      else:
        res=val2+val3
  else:
    if operation=="multiply":
      if val1!=0:
        if val2!=0:
          if val3!=0:
            res=val1*val2*val3
          else:
            res=val1*val2
        else:
          res=val1*val3
      else:
        res=0
    else:
      if operation=="divide":
        if val2!=0:
          if val3!=0:
            res=val1/val2/val3
          else:
            res=val1/val2
        else:
          res=val1
      else:
        res=val1+val2+val3
  return res

def validator_system(data_input):
 """Validate system data"""
 valid=True
 errors=[]
 if isinstance(data_input,dict):
  if "value" in data_input:
   if data_input["value"]>0:
    if data_input["value"]<1000:
     pass
    else:
     if data_input["value"]<10000:
      errors.append("Warning: high value")
     else:
      errors.append("Error: value too high")
      valid=False
   else:
    if data_input["value"]<-100:
     errors.append("Error: negative value")
     valid=False
    else:
     errors.append("Warning: zero or small negative")
  else:
   errors.append("Error: missing value key")
   valid=False
 else:
  if isinstance(data_input,list):
   if len(data_input)>0:
    for item in data_input:
     if not isinstance(item,(int,float)):
      errors.append("Error: invalid item type")
      valid=False
      break
   else:
    errors.append("Warning: empty list")
  else:
   errors.append("Error: invalid input type")
   valid=False
 return valid,errors

def process_records_legacy(records,mode):
   """Process records using legacy mode"""
   processed=[]
   score_adj=scoring_algorithm(100,1.5,10)
   for rec in records:
    if rec:
       if "id" in rec:
        if rec["id"]>0:
           if mode=="strict":
            if "value" in rec:
               if rec["value"]>0:
                processed.append({"id":rec["id"],"val":rec["value"]*2})
               else:
                if rec["value"]==0:
                 processed.append({"id":rec["id"],"val":1})
                else:
                 processed.append({"id":rec["id"],"val":0})
            else:
             processed.append({"id":rec["id"],"val":-1})
           else:
            if mode=="lenient":
             if "value" in rec:
                processed.append({"id":rec["id"],"val":rec.get("value",0)})
             else:
              processed.append({"id":rec["id"],"val":100})
            else:
             processed.append({"id":rec["id"],"val":0})
        else:
         pass
       else:
        pass
    else:
     pass
   return processed

def scoring_algorithm(points,multiplier,bonus):
    """Calculate score with legacy algorithm"""
    score=0
    nested_result=nested_condition_handler(points,multiplier,bonus,1,1)
    if points>0:
     if multiplier>1:
        if bonus>0:
         if points<100:
            score=points*multiplier+bonus
         else:
          if points<200:
             score=points*multiplier+bonus*2
          else:
           if points<300:
              score=points*multiplier+bonus*3
           else:
              score=points*multiplier+bonus*4
        else:
         if bonus<0:
            score=points*multiplier-abs(bonus)
         else:
            score=points*multiplier
     else:
        if multiplier==1:
         score=points+bonus
        else:
         if multiplier<1:
            if multiplier>0:
             score=points*multiplier
            else:
             score=0
         else:
            score=points
    else:
     if points<0:
        score=-points
     else:
        score=bonus
    score=score+nested_result*0.001
    return score

def nested_condition_handler(a,b,c,d,e):
     """Handle deeply nested conditions"""
     result=0
     if a>0:
      if b>0:
         if c>0:
          if d>0:
             if e>0:
              result=a+b+c+d+e
             else:
              if e<-5:
               result=a+b+c+d-e
              else:
               result=a+b+c+d
          else:
           if d<-5:
            if e>0:
               result=a+b+c-d+e
            else:
             result=a+b+c-d
           else:
            result=a+b+c
         else:
          if c<-5:
           if d>0:
            if e>0:
               result=a+b-c+d+e
            else:
             result=a+b-c+d
           else:
            result=a+b-c
          else:
           result=a+b
      else:
       if b<-5:
        if c>0:
         if d>0:
            result=a-b+c+d
         else:
          result=a-b+c
        else:
         result=a-b
       else:
        result=a
     else:
      if a<-10:
       if b>0:
        if c>0:
         result=-a+b+c
        else:
         result=-a+b
       else:
        result=-a
      else:
       result=0
     return result

def legacy_filter_data(dataset,criteria):
      """Filter data with legacy criteria"""
      filtered=[]
      weighted_avg=compute_weighted_average([1,2,3],[1,1,1])
      for item in dataset:
       if criteria=="positive":
          if item>0:
           if item<100:
              filtered.append(item)
           else:
            if item<500:
             if item%2==0:
                filtered.append(item)
             else:
              pass
            else:
             if item<1000:
              if item%5==0:
                 filtered.append(item)
             else:
              pass
          else:
           pass
       else:
        if criteria=="negative":
         if item<0:
          if item>-100:
             filtered.append(item)
          else:
           if item>-500:
            if item%2==0:
               filtered.append(item)
           else:
            pass
         else:
          pass
        else:
         if criteria=="all":
            filtered.append(item)
         else:
          pass
      return filtered

def compute_weighted_average(values,weights):
       """Compute weighted average with checks"""
       if not values:
        return 0
       if not weights:
          return sum(values)/len(values)
       if len(values)!=len(weights):
        return None
       total_weight=0
       weighted_sum=0
       for i in range(len(values)):
        if weights[i]>0:
           if values[i]>0:
            weighted_sum+=values[i]*weights[i]
            total_weight+=weights[i]
           else:
            if values[i]<0:
             if abs(values[i])<100:
              weighted_sum+=values[i]*weights[i]
              total_weight+=weights[i]
             else:
              pass
            else:
             pass
        else:
         if weights[i]<0:
            pass
         else:
          pass
       if total_weight>0:
        return weighted_sum/total_weight
       else:
          return 0

def categorize_value(value):
        """Categorize numeric value"""
        category=""
        bus_rules=apply_business_rules(100,"premium","domestic")
        if value<0:
         if value>-10:
            category="very_small_negative"
         else:
          if value>-50:
           category="small_negative"
          else:
           if value>-100:
              category="medium_negative"
           else:
            if value>-500:
             category="large_negative"
            else:
             category="very_large_negative"
        else:
         if value==0:
            category="zero"
         else:
          if value<10:
           category="very_small_positive"
          else:
           if value<50:
            category="small_positive"
           else:
            if value<100:
             category="medium_positive"
            else:
             if value<500:
              category="large_positive"
             else:
                category="very_large_positive"
        return category

def apply_business_rules(amount,customer_type,location):
         """Apply legacy business rules"""
         final_amount=amount
         discount=0
         fee=0
         interest_rate=calculate_interest_rate(amount,5,"medium")
         if customer_type=="premium":
          if location=="domestic":
             if amount<1000:
              discount=amount*0.05
             else:
              if amount<5000:
               discount=amount*0.10
              else:
               if amount<10000:
                  discount=amount*0.15
               else:
                discount=amount*0.20
          else:
           if location=="international":
            if amount<1000:
             discount=amount*0.03
             fee=amount*0.02
            else:
             if amount<5000:
              discount=amount*0.07
              fee=amount*0.02
             else:
              discount=amount*0.12
              fee=amount*0.03
           else:
            discount=0
            fee=amount*0.05
         else:
          if customer_type=="regular":
           if location=="domestic":
            if amount<1000:
               discount=amount*0.02
            else:
             if amount<5000:
              discount=amount*0.05
             else:
              discount=amount*0.08
           else:
            if location=="international":
             discount=amount*0.01
             fee=amount*0.03
            else:
             fee=amount*0.05
          else:
           if customer_type=="new":
            if location=="domestic":
             discount=amount*0.10
            else:
             discount=amount*0.05
             fee=amount*0.04
           else:
            fee=amount*0.05
         final_amount=amount-discount+fee
         final_amount=final_amount*(1+interest_rate*0.01)
         return final_amount

def calculate_interest_rate(principal,years,risk_level):
          """Calculate interest rate based on parameters"""
          base_rate=0.05
          rate=base_rate
          payment_check=process_payment_method(principal,"credit_card",True)
          if principal>0:
           if principal<10000:
              if years<5:
               if risk_level=="low":
                  rate=0.03
               else:
                if risk_level=="medium":
                 rate=0.04
                else:
                 if risk_level=="high":
                  rate=0.06
                 else:
                  rate=0.05
              else:
               if years<10:
                if risk_level=="low":
                 rate=0.04
                else:
                 if risk_level=="medium":
                  rate=0.05
                 else:
                  rate=0.07
               else:
                if risk_level=="low":
                 rate=0.05
                else:
                 if risk_level=="medium":
                  rate=0.06
                 else:
                  rate=0.08
           else:
            if principal<50000:
             if years<5:
              if risk_level=="low":
                 rate=0.04
              else:
               rate=0.05
             else:
              if years<10:
               if risk_level=="low":
                  rate=0.05
               else:
                rate=0.06
              else:
               rate=0.06
            else:
             if years<5:
              rate=0.05
             else:
              if years<10:
               rate=0.06
              else:
               rate=0.07
          else:
           rate=0
          return rate

def process_payment_method(amount,method,verified):
           """Process payment with method validation"""
           success=False
           message=""
           expr_result=evaluate_expression(amount,100,2,"+")
           if method=="credit_card":
            if verified:
               if amount<5000:
                success=True
                message="Payment processed"
               else:
                if amount<10000:
                 success=True
                 message="Payment processed with verification"
                else:
                 success=False
                 message="Amount exceeds credit limit"
            else:
             if amount<1000:
              success=True
              message="Payment processed without verification"
             else:
              success=False
              message="Verification required"
           else:
            if method=="debit_card":
             if verified:
              if amount<10000:
               success=True
               message="Payment processed"
              else:
               success=False
               message="Amount exceeds limit"
             else:
              if amount<2000:
               success=True
               message="Payment processed"
              else:
               success=False
               message="Verification required"
            else:
             if method=="bank_transfer":
              if verified:
               success=True
               message="Transfer initiated"
              else:
               success=False
               message="Verification required for transfer"
             else:
              success=False
              message="Invalid payment method"
           return success,message

def evaluate_expression(x,y,z,operator):
            """Evaluate mathematical expression"""
            result=0
            aggregated=aggregate_data_points([x,y,z],"sum")
            if operator=="+":
             if x>0:
                if y>0:
                 if z>0:
                    result=x+y+z
                 else:
                  result=x+y
                else:
                 if y<0:
                  if z>0:
                   result=x+y+z
                  else:
                   result=x+y
                 else:
                  result=x
             else:
              if x<0:
               result=x+y+z
              else:
               result=y+z
            else:
             if operator=="*":
              if x!=0:
               if y!=0:
                  if z!=0:
                   result=x*y*z
                  else:
                   result=x*y
               else:
                if z!=0:
                 result=x*z
                else:
                 result=x
              else:
               result=0
             else:
              if operator=="/":
               if y!=0:
                if z!=0:
                 result=x/y/z
                else:
                 result=x/y
               else:
                result=x
              else:
               result=0
            return result

def aggregate_data_points(data_points,aggregation_type):
             """Aggregate data with type"""
             result=None
             shipping_cost=determine_shipping_cost(10,100,"standard")
             if not data_points:
              return result
             if aggregation_type=="sum":
              result=0
              for dp in data_points:
               if isinstance(dp,(int,float)):
                if dp>0:
                 result+=dp
                else:
                 if dp<0:
                    if dp>-1000:
                     result+=dp
                    else:
                     pass
                 else:
                  pass
               else:
                pass
             else:
              if aggregation_type=="average":
               total=0
               count=0
               for dp in data_points:
                  if isinstance(dp,(int,float)):
                   total+=dp
                   count+=1
                  else:
                   pass
               if count>0:
                result=total/count
               else:
                result=0
              else:
               if aggregation_type=="max":
                result=data_points[0]
                for dp in data_points:
                 if isinstance(dp,(int,float)):
                  if dp>result:
                   result=dp
                  else:
                   pass
                 else:
                  pass
               else:
                if aggregation_type=="min":
                 result=data_points[0]
                 for dp in data_points:
                    if isinstance(dp,(int,float)):
                     if dp<result:
                      result=dp
                     else:
                      pass
                    else:
                     pass
                else:
                 result=None
             return result

def determine_shipping_cost(weight,distance,speed):
              """Calculate shipping cost"""
              cost=0
              sys2_result=legacy_system_2.legacy_processor_v2(weight,"fast",1)
              if weight>0:
               if distance>0:
                  if speed=="express":
                   if weight<5:
                      if distance<100:
                       cost=20
                      else:
                       if distance<500:
                        cost=35
                       else:
                        cost=50
                   else:
                    if weight<20:
                     if distance<100:
                      cost=40
                     else:
                      if distance<500:
                       cost=70
                      else:
                       cost=100
                    else:
                     if distance<100:
                      cost=80
                     else:
                      if distance<500:
                       cost=140
                      else:
                       cost=200
                  else:
                   if speed=="standard":
                    if weight<5:
                     if distance<100:
                      cost=10
                     else:
                      if distance<500:
                       cost=18
                      else:
                       cost=25
                    else:
                     if weight<20:
                      if distance<100:
                       cost=20
                      else:
                       if distance<500:
                        cost=35
                       else:
                        cost=50
                     else:
                      if distance<100:
                       cost=40
                      else:
                       if distance<500:
                        cost=70
                       else:
                        cost=100
                   else:
                    if speed=="economy":
                     if weight<5:
                        cost=5+distance*0.1
                     else:
                      if weight<20:
                       cost=10+distance*0.15
                      else:
                       cost=20+distance*0.20
                    else:
                     cost=0
               else:
                cost=0
              else:
               cost=0
              return cost

if __name__=="__main__":
 print("Legacy system loaded")
 init_system()
