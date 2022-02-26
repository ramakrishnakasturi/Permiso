#include <bits/stdc++.h>
#include<iostream>
#include<string>
#include<vector>
using namespace std;
string firstof(char f1,vector<string> s,string r)
{  
    string s2;
    for(int i=0;i<s.size();i++)
    {
      string s1=s[i];
      if(f1==s1[0])
      {
        s2=s1;
        break;
      }
    }
    int flag=0;
    for(int j=3;j<s2.length();j++)
    {
        if(97<=s2[j] && s2[j]<=122 && flag==0)
        {
          r=r+s2[j];
          flag=1;
        }
        if(s2[j]=='/')
        flag=0;
        else if(65<=s2[j] && s2[j]<=90 && flag==0){
          r=r+firstof(s2[j],s,r);
          int y=0;
          for(int k=0;k<r.length();k++){
            if(r[k]=='#'){
              y=1;
              break;
            }
          }
          r=r+firstof(s2[j+1],s,r);
          flag=1;
        }
        else if(s2[j]=='#' && flag==0){
          r+='#';
          flag=1;
        }
       
    }
  return r;
}
string follow(char ch,vector<string> s,string r)
{
    for(int i=0;i<s.size();i++)
    {
        for(int j=3;j<s[i].length();j++)
        {
            if(s[i][j]==ch)
            {
                if(s[i][j+1]=='\0' || s[i][j+1]=='/')
                {
                   if(s[i][j]==s[i][0])
                  {
                     continue;
                  }
                   else
                   {  
                      r+=follow(s[i][0],s,r);
                   }
                   
                }
                else if(s[i][j+1]>=65 && s[i][j+1]<=90)
                {
                  string o=firstof(s[i][j+1],s,r);
                  for(int k=0;k<o.length();k++)
                  {
                    if(o[k]=='#')
                    {
                      if(s[i][j+2]=='\0')
                      {
                        r=r+follow(s[i][0],s,r);
                      }
                      else if(s[i][j+2]>=97 && s[i][j+2]<=122)
                      {
                        r=r+s[i][j+2];
                      }
                      else
                      {
                        r=r+firstof(s[i][j+2],s,r);
                      }
                    }
                    else
                    {
                      r=r+o[k];
                    }
                  }
                }
                else if(s[i][j+1]>=97 && s[i][j+1]<=122)
                {
                    r=r+s[i][j+1];
                }
            }
        }
    }
    return r;
}
string unique(string str) {
    for (int i = 0; i < str.size(); i++) {
        while (true) {
            int j = str.find_last_of(str[i]);
            if (i < j) {
                str.erase(j, 1);
            } else {
                break;
            }
        }
    }
    return str;
}
int main(){
  int n;
  cin>>n;
  vector<string> s(n);
  vector<string> first(n);
  cout<<"enter the productions without left recursion"<<"\n";
  for(int i=0;i<n;i++){
    cin>>s[i];
  }
  for(int i=0;i<n;i++)
  {
      string f1=s[i];
      string r="",x="";
      first[i]=firstof(f1[0],s,r);
      cout<<"first of "<<f1[0] <<"is "<<" "<< unique(first[i])
      <<"\n";
  }
  string arr;
  for(int i=0;i<s.size();i++)
  {
      string q=s[i];
      for(int j=0;j<q.length();j++)
      {
         if(q[j]>=65 && q[j]<=90)
         {
             arr+=q[j];
         }
      }
  }
  string l=unique(arr);
for(int i=0;i<l.length();i++)
{
   if(i==0)
{
 cout<<"Follow of "<<l[i]<<" "<<unique(follow(l[i],s,"$"))<<endl;
}
else
{
cout<<"Follow of "<<l[i]<<" "<<unique(follow(l[i],s,""))<<endl;
}
}
  return 0;
}

