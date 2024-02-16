import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Injectable } from '@angular/core';
import { HttpClient, HttpRequest, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

interface Period {
  value: string;
  viewValue: string;
}

@Component({
      selector: 'app-fileupload',
      templateUrl: './fileupload.component.html',
      styleUrls: ['./fileupload.component.css']
    })

@Injectable({
  providedIn: 'root'
})

export class FileuploadComponent {
  selected: string = "";
  predictvalue: string="";
  selectedFile: any = null;
 
  constructor(private http: HttpClient, private router:Router) {}

  onFileChanged(event: any) {
    this.selectedFile = event.target.files[0];
  }
 
  onpredict(){
 
    if (!this.selectedFile) {
      console.error("No file selected");
      return;
    }
  
    if (!this.selected) {
      console.error("No period selected");
      return;
    }
  
    if (!this.predictvalue) {
      console.error("No predict value selected");
      return;
    }
    console.log(this.selected);
    console.log(this.predictvalue);
    const formData = new FormData();
    formData.append('file', this.selectedFile, this.selectedFile.name);
    formData.append('period', this.selected);
    formData.append('range', this.predictvalue);

  
    this.http.post('http://localhost:5000/', formData).subscribe(
      (response) => {
        console.log(response);
        this.router.navigate(['/result']);
      },
      (error) => {
        console.error(error);
      }
    );
    
    }
    navigateToCluster() {
      if (!this.selectedFile) {
        console.error("No file selected");
        return;
      }
  
      const formData = new FormData();
      formData.append('file', this.selectedFile, this.selectedFile.name);
      formData.append('num_clusters', this.predictvalue);
  
      // Adjust the POST request to the correct endpoint
      this.http.post('http://localhost:5000/cluster', formData).subscribe(
        (response: any) => {
          console.log(response);
          this.router.navigate(['/cluster']);  // Navigate to the cluster page
        },
        (error) => {
          console.error(error);
        }
      );
    }
    
  }


  

