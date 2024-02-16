import { Component } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  signupusers: any[] = [];
  signupobj: any ={
    username: '',
    email: '',
    password: ''
  };
  loginobj:any ={
    username: '',
    password: ''
  };
  
    
  
  constructor(private router:Router){ }
  
  ngOnInit(): void {
    const localData =localStorage.getItem('signupusers');
    if(localData !=null){
      this.signupusers = JSON.parse(localData);
    }
  }
  onsignup(){
  this.signupusers.push(this.signupobj);
  localStorage.setItem('signupusers',JSON.stringify(this.signupusers));
  alert('user signin successfully');
  this.signupobj  ={
    username: '',
    email: '',
    password: ''
  };
}
onlogin(){
  debugger
  const isuserexist =this.signupusers.find(m => m.username == this.loginobj.username && m.password == this.loginobj.password);
  if(isuserexist != undefined){
    alert('user login successfully');
    this.router.navigate(['fileupload'])
  }else{
    alert('wrong credentials');
  }
  }
}
