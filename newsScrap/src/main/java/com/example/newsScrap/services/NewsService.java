package com.example.newsScrap.services;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.newsScrap.entities.News;
import com.example.newsScrap.repository.ArticulosRepository;


@Service
public class NewsService implements INewsService{
	
	@Autowired
	private ArticulosRepository repository;
	
	@Override
	public List<News> getAll(){
		return (List<News>) repository.findAll();
	}

	@Override
	public News getById(Long id) {
		// TODO Auto-generated method stub
		return (News) repository.findById(id).get();
	}
	
}
