using UnityEngine;

public class Jump : MonoBehaviour
{
    public Vector2 JumpForce;
    
    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            GetComponent<Rigidbody2D>().AddForce(JumpForce);
            GetComponent<AudioSource>().Play();
        }
    }
}
