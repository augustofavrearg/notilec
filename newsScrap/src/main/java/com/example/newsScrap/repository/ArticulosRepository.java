package com.example.newsScrap.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.newsScrap.entities.News;

@Repository
public interface ArticulosRepository extends CrudRepository <News, Long> {

}
