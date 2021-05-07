<?php namespace App\Controllers;

use App\Models\BlogModel;

class Blog extends BaseController
{


  function post($slug){
			$model = new BlogModel();
			$data['post'] = $model->getPosts($slug);

			echo view('templates/header', $data);
			echo view('blog/post');
			echo view('templates/footer');
  }

	function create(){
		helper('form');
		$model = new BlogModel();

		if(! $this->validate([
			 'title' => 'required|min_length[3]|max_length[255]',
			 'body' => 'required'
			])) {
				echo view('templates/header');
				echo view('blog/create');
				echo view('templates/footer');
		}
		else{
			$model->save(
			[
				'title' => $this->request->getVar('title'),
				'body' => $this->request->getVar('body'),
				'slug' => url_title($this->request->getVar('title')),
        'author' => session() ->get('firstname').' '.session() ->get('lastname'),
        'author_id' => session() ->get('id'),
			]
			);

			$session = \Config\Services::session();
			$session->setFlashdata('success', 'New post was created!');
			return redirect()->to('/');
		}
	}

	function delete($id){
		helper('form');
		$model = new BlogModel();
		$model->delete($id);
		$session = \Config\Services::session();
		$session->setFlashdata('success', 'Post was deleted!');
		return redirect()->to('/');
	}

	function edit($slug){
		helper('form');
		$model = new BlogModel();
		$data['post'] = $model->getPosts($slug);
		echo view('templates/header', $data);
		echo view('blog/edit');
		echo view('templates/footer');
	}

  function update($slug,$id){
    helper('form');
		$model = new BlogModel();

    if(! $this->validate([
			 'title' => 'required|min_length[3]|max_length[255]',
			 'body' => 'required'
			])) {
        $data['post'] = $model->getPosts($slug);
        echo view('templates/header', $data);
    		echo view('blog/edit');
    		echo view('templates/footer');
		}
    else{
    $data = [
  				'title' => $this->request->getVar('title'),
  				'body' => $this->request->getVar('body'),
  				'slug' => url_title($this->request->getVar('title')),
            ];
    $model->update($id, $data);
    $session = \Config\Services::session();
		$session->setFlashdata('success', 'Post was updated!');
    return redirect()->to('/');
  }}

	//--------------------------------------------------------------------

}
