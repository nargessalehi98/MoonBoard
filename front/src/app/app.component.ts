import {AfterViewInit, Component, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, AfterViewInit {
constructor(private http:HttpClient){}

  rows: any[] = []
  letters: string[] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'];
  activeNode:any = {
    grade: "7B",
    start: ["2J"],
    body: ["7E", "11H", "14A", "16E", "17B", "17C", "17K"],
    top: ["18J"]
  }

  ngOnInit(): void {
    this.initBoard();
  }

  ngAfterViewInit() {
  this.http.get("http://127.0.0.1:8000/route/").subscribe(res=>{
  this.activeNode = res;
    ['start', 'body', 'top'].forEach(pos => this.setActive(pos))
  })
  }

  initBoard() {
    for (let i = 18; i > 0; i--) {
      const images: string[] = [];
      this.letters.forEach(lt => {
        images.push(`assets/images/${i}/${i}${lt}.png`)
      })
      this.rows.push({rowNum: i, images});
    }
  }

  setActive(pos: string) {
    this.activeNode[pos].forEach(selector => {
      const el = document.querySelector(`#item-${selector}`);
      el.classList.add(pos);
    })
  }
}
