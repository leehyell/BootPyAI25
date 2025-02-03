package edu.mbcai.pybootai.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
    @GetMapping("/")
    public String home() {
        //resources/templates/index.html을 찾아감.
        return "index";
    }//http://localhost:8010에 반응하는 컨트롤러. → 테스트 완료.
}