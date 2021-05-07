<?php namespace App\Controllers;

use App\Models\BlogModel;
use App\Models\UserModel;

class Users extends BaseController
{
	 function login()
	{
		$data = [];
		helper(['form']);

		if ($this->request->getMethod() == 'post') {
			$rules = [
				'email' => 'required|min_length[6]|max_length[50]|valid_email',
				'password' => 'required|min_length[8]|max_length[255]|validateUser[email,password]',
			];

			$errors = [
				'password' => [
					 'validateUser' => 'Email or Password don\'t match'
				]
			];
			$model = new UserModel();
			$user = $model->where('email', $this->request->getVar('email'))
										->first();
			if (! $this->validate($rules, $errors)){
				$data['validation'] = $this->validator;
			}
		 else{
				$model = new UserModel();
				$user = $model->where('email', $this->request->getVar('email'))
											->first();
											if($user['is_logged']==1){
												$session = session();
												$session->setFlashdata('success', 'Allery loged in other browser');
												return redirect()->to('/');
												
											}
												else{
			  $this->setUserSession($user);

				$session = session();
				$session->setFlashdata('success', 'Successful Login');
				$newData = [
					'id' => session()->get('id'),
					'is_logged' => '1',
				];
				$model->save($newData);
				return redirect()->to('/'); }
			}
		}


		echo view('templates/header',$data);
		echo view('user/login',);
		echo view('templates/footer');
	}
	private function setUserSession($user){
		$data = [
			'id' => $user['id'],
			'firstname' => $user['firstname'],
			'lastname' => $user['lastname'],
			'email' => $user['email'],
			'isLoggedIn' => true,
		];

		session()->set($data);
		return true;
	}

	function register(){
		$data = [];
		helper(['form']);

		if ($this->request->getMethod() == 'post') {
			$rules = [
				'firstname' => 'required|min_length[3]|max_length[20]',
				'lastname' => 'required|min_length[3]|max_length[20]',
				'email' => 'required|min_length[6]|max_length[50]|valid_email|is_unique[users.email]',
				'password' => 'required|min_length[8]|max_length[255]',
				'password_confirm' => 'matches[password]',
			];
			if (! $this->validate($rules)){
				$data['validation'] = $this->validator;
			}else{
				$model = new UserModel();
				$newData = [
					'firstname' => $this->request->getVar('firstname'),
					'lastname' => $this->request->getVar('lastname'),
					'email' => $this->request->getVar('email'),
					'password' => $this->request->getVar('password'),
				];
				$model->save($newData);
				$session = session();
				$session->setFlashdata('success', 'Successful Registration');
				return redirect()->to('/');
			}
		}

		echo view('templates/header',$data);
		echo view('user/register');
		echo view('templates/footer');
	}

	function profile(){
		$Data = [];
		helper(['form']);
		$model = new UserModel();
		$id = session()->get('id');

		if ($this->request->getMethod() == 'post') {
			$rules = [
				'firstname' => 'required|min_length[3]|max_length[20]',
				'lastname' => 'required|min_length[3]|max_length[20]',
			];

			if($this->request->getPost('password') != ''){
				$rules['password'] = 'required|min_length[8]|max_length[255]';
				$rules['password_confirm'] = 'matches[password]';
			}

			if (! $this->validate($rules)){
				$data['validation'] = $this->validator;
			}else{

				$newData = [
					'id' => session()->get('id'),
					'firstname' => $this->request->getVar('firstname'),
					'lastname' => $this->request->getVar('lastname'),
				];
				if($this->request->getPost('password') != ''){
					$newData['password'] = $this->request->getVar('password');
				}
				$model->save($newData);
				session()->setFlashdata('success', 'Successful Updated');
				return redirect()->to('/user/profile');
			}
		}


		$data['user'] = $model->where('id', session()->get('id'))->first();
		echo view('templates/header',$data);
		echo view('user/profile');
		echo view('templates/footer');
	}

	function logout(){
		$model = new UserModel();
		$newData = [
			'id' => session()->get('id'),
			'is_logged' => '0',
		];
		$model->save($newData);
		session()->destroy();
		return redirect()->to('/');
	}



	//--------------------------------------------------------------------

}
