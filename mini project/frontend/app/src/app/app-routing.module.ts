import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FileuploadComponent } from './fileupload/fileupload.component';
import { LoginComponent } from './login/login.component';
import { ResultComponent } from './result/result.component';
import { ClusterComponent } from './cluster/cluster.component';
const routes: Routes = [
  {
    path: '',component:LoginComponent
  },{
    path: 'fileupload',component:FileuploadComponent
  },{
    path: 'result',component:ResultComponent
  },{
    path: 'cluster',component:ClusterComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  declarations: [
    ResultComponent
  ]
})
export class AppRoutingModule { }
