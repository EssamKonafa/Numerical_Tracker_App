import axios from 'axios'
import React, { useEffect, useState } from 'react'

function Home() {

  const [numValue, setNumValue] = useState('')
  const [storedNum, setStoredNum] = useState('')

  const getNumValues = async () => {
    try {
      const response = await axios.get('http://localhost:5000/getNumValues')
      setStoredNum(response.data.numerical_value)
    } catch (err) {
      console.error(err);
    }
  }

  const handleAddNum = async () => {
    try {
      await axios.post('http://localhost:5000/saveNumValue', { numerical_value: numValue })
      getNumValues()
    } catch (err) {
      console.error(err);
    }
  }

  const handleChange = (event) => {
    const value = event.target.value
    setNumValue(value)
  }

  const calcPercent = () => {
    const percent = (numValue / storedNum) * 100
    return percent ? percent.toFixed(2) : ''
  }

  useEffect(() => {
    getNumValues()
  }, [storedNum])

  return (
    <div className='flex pt-10 justify-center'>
      <table className='border-black border-2 text-center '>
        <thead>
          <tr >
            <th className='border-r-2 border-b-2 border-black p-3'>Numerical Value</th>
            <th className='border-r-2 border-b-2 border-black px-5'>Existing Value</th>
            <th className='px-5 border-b-2 border-black'>Percentage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className='py-5 m-5 border-r-2 border-black'>
              <input className='border-2 rounded-lg m-2 text-center py-1' type='number' value={numValue} onChange={handleChange} />

              <button className='mx-2 rounded-lg p-2 bg-gray-200 hover:bg-black hover:text-white transition-all' onClick={handleAddNum}>Add</button>

            </td>
            <td className='border-r-2 border-black'>{storedNum}</td>
            <td>{calcPercent()}%</td>
          </tr>
        </tbody>
      </table>
    </div>
  )
}

export default Home