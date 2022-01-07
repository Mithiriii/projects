using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{

    public float speed = 12f;
    public float gravity = -9.81f;
    Vector3 velocity;
    public CharacterController controller;
    public Transform groundCheck;
    public float groundDistance = 0.4f;
    public LayerMask groundMask;
    private bool isGrounded;
    private AudioSource audioSource;
    private bool isMoving = false;

    // Start is called before the first frame update
    void Start()
    {
        audioSource = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {
        isGrounded = Physics.CheckSphere(groundCheck.position, groundDistance, groundMask);
        if(isGrounded && velocity.y < 0)
        {
            velocity.y = -2f;
        }
        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");

        if (x >= 0.01f || z >= 0.01f || x <= -0.01f || z <= -0.01f)
            isMoving = true;
        else
            isMoving = false;
        MakeStepSound();

        Vector3 move = transform.right * x + transform.forward * z;

        controller.Move(move * speed * Time.deltaTime);
        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }

    private void MakeStepSound()
    {
        if (isMoving)
        {
            if (!audioSource.isPlaying)
                audioSource.Play();
        }
        else
            audioSource.Stop();
    }
}
