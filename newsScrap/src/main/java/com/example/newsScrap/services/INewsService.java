package com.example.newsScrap.services;

import java.util.List;

import com.example.newsScrap.entities.News;

public interface INewsService {
	public List<News> getAll();

	public News getById(Long id);
}
