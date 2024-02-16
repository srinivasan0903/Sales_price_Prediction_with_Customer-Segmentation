// import { Component } from '@angular/core';

// @Component({
//   selector: 'app-cluster',
//   templateUrl: './cluster.component.html',
//   styleUrls: ['./cluster.component.css']
// })
// export class ClusterComponent {

// }

// import { HttpClient } from '@angular/common/http';
// import { Component, OnInit } from '@angular/core';

// @Component({
//   selector: 'app-cluster',
//   templateUrl: './cluster.component.html',
//   styleUrls: ['./cluster.component.css']
// })
// export class ClusterComponent implements OnInit {
//   highSalesClusters: any[] | undefined;

//   constructor(private http: HttpClient) {}

//   ngOnInit(): void {
//     // Make a request to fetch the high sales clusters data
//     this.http.get<any[]>('http://127.0.0.1:5000/cluster').subscribe(
//       (data: any[]) => {
//         this.highSalesClusters = data;
//         console.log('High Sales Clusters:', this.highSalesClusters);
//       },
//       (error) => {
//         console.error('Error fetching high sales clusters:', error);
//       }
//     );
//   }
// }

import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cluster',
  templateUrl: './cluster.component.html',
  styleUrls: ['./cluster.component.css']
})
export class ClusterComponent implements OnInit {
  highSalesClusters: any[] | undefined;
  csvData: string | undefined;
  

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    // Make a request to fetch the high sales clusters data
    this.http.get<any[]>('http://127.0.0.1:5000/cluster').subscribe(
      (data: any[]) => {
        this.highSalesClusters = data;
        console.log('High Sales Clusters:', this.highSalesClusters);
      },
      (error) => {
        console.error('Error fetching high sales clusters:', error);
      }
    );

   
    // Make a request to fetch the CSV data
    this.http.get('http://127.0.0.1:5000/high_sales_clusters_csv', { responseType: 'text' }).subscribe(
      (data: string) => {
        this.csvData = data;
        console.log('CSV Data:', this.csvData);
      },
      (error) => {
        console.error('Error fetching CSV data:', error);
      }
    );
  }
}




