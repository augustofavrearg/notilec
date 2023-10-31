package com.example.newsScrap.controllers;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.example.newsScrap.entities.News;
import com.example.newsScrap.services.INewsService;

@RestController
public class NewsController {
	
	@Autowired
	private INewsService service;
	
	@GetMapping("/api/noticias")
	public List<News> getAll(){
		return service.getAll();
	}
	
	@GetMapping("/api/noticias/{id}")
	public News getById(@PathVariable String id){
		return service.getById(Long.parseLong(id));
	}
}
